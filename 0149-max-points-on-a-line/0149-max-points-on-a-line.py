class Solution:
    def maxPoints(self, points):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        if len(points) <= 2:
            return len(points)

        answer = 0

        for i in range(len(points)):
            slopes = {}

            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                g = gcd(dx, dy)

                dx //= g
                dy //= g

                # Make the slope representation consistent
                if dx < 0:
                    dx = -dx
                    dy = -dy

                if dx == 0:
                    dy = 1

                slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

            if slopes:
                answer = max(answer, max(slopes.values()) + 1)

        return answer