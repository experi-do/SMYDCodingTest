T = str(input())
P = str(input())

def makeLps(p):
    tmpTable = [0] * len(p)  # 초기화: LPS 배열 전부 0
    j = 0  # 현재 비교 중인 접두사 길이

    for i in range(1, len(p)):  # i는 현재 위치
        while j > 0 and p[i] != p[j]:
            # 현재 문자가 다르면 이전 접두사로 돌아감
            j = tmpTable[j - 1]

        if p[i] == p[j]:
            # 문자가 같으면 j 증가
            j += 1
            tmpTable[i] = j  # i번째 위치의 LPS 값 저장

    return tmpTable


def kmp(t, p):  # 텍스트 t에서 패턴 p를 찾아, 일치하는 시작 위치들을 반환하는 함수
    lps = makeLps(p)  # 패턴의 LPS 배열 생성
    result = []
    j = 0             # p의 현재 인덱스

    for i in range(len(t)):
        # 패턴과 현재 문자가 다를 경우, j를 이전까지 일치한 접두사 길이로 이동시켜 비교 재시도
        while j > 0 and t[i] != p[j]:
            j = lps[j - 1]

        # 문자가 일치할 경우, 패턴 포인터 j를 증가
        if t[i] == p[j]:
            j += 1
            # 패턴 전체가 일치했을 경우 (j == 패턴 길이)
            if j == len(p):
                # result에 일치 시작 위치 저장
                result.append(i - j + 2)
                # j를 이전 LPS 값으로 갱신
                j = lps[j - 1]

    return result


res = kmp(T, P)
print(len(res))
print(' '.join(map(str, res)))