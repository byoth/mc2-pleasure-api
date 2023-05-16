import numpy as np
from haversine import haversine
from pin_clusters.models import PinCluster

def get_radius(latitude_delta, longitude_delta):
    if not latitude_delta or not longitude_delta:
        return 0

    return min(float(latitude_delta), float(longitude_delta)) * 10

def get_pin_clusters(pins, radius):
    # pin의 개수가 0이면 빈 리스트 반환
    if len(pins) == 0:
        return []

    # pin의 위치 정보를 numpy array로 변환
    pin_locations = np.array([(min(max(pin.latitude, -90), 90), min(max(pin.longitude, -180), 180)) for pin in pins])

    # 거리 계산 함수 설정
    dist = haversine

    # 거리 행렬 계산
    dist_matrix = np.zeros((len(pins), len(pins)))
    for i in range(len(pins)):
        for j in range(i, len(pins)):
            dist_matrix[i][j] = dist(pin_locations[i], pin_locations[j])
            dist_matrix[j][i] = dist_matrix[i][j]

    # 클러스터링
    clusters = []
    visited = set()
    for i in range(len(pins)):
        if i in visited:
            continue

        # 새로운 클러스터 생성
        new_cluster = [i]
        visited.add(i)

        # 현재 pin으로부터 거리가 radius 이내인 모든 pin을 클러스터에 추가
        for j in range(i+1, len(pins)):
            if dist_matrix[i][j] < radius:
                new_cluster.append(j)
                visited.add(j)

        # 클러스터 객체 생성
        main_pin = pins[new_cluster[0]]
        pin_ids = map(lambda p: pins[p].id, new_cluster)
        pins_count = len(new_cluster)
        latitude = np.mean(pin_locations[new_cluster, 0])
        longitude = np.mean(pin_locations[new_cluster, 1])
        cluster = PinCluster(main_pin, pin_ids, pins_count, latitude, longitude)

        # 클러스터 추가
        clusters.append(cluster)

    return clusters
