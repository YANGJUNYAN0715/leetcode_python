class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tot, num = 0, 0
                for x in range(max(i - 1, 0), min(i + 2, m)):
                    for y in range(max(j - 1, 0), min(j + 2, n)):
                        tot += img[x][y]
                        num += 1
                # 需要向下取整
                ans[i][j] = tot // num
        return ans


if __name__ == '__main__':
    s = Solution()
    img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    print(s.imageSmoother(img))
