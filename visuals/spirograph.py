import math


def spirograph(R, r, d, points=2000):
    coords = []
    for i in range(points + 1):
        t = i * 2 * math.pi / points
        x = (R - r) * math.cos(t) + d * math.cos((R - r) / r * t)
        y = (R - r) * math.sin(t) - d * math.sin((R - r) / r * t)
        coords.append((x, y))
    return coords


def to_path(coords):
    start = coords[0]
    path = [f"M {start[0]:.3f},{start[1]:.3f}"]
    for x, y in coords[1:]:
        path.append(f"L {x:.3f},{y:.3f}")
    return " ".join(path)


def main():
    coords = spirograph(125, 75, 125)
    path = to_path(coords)
    html = f"""<!DOCTYPE html>
<html lang='en'>
<head>
<meta charset='UTF-8'>
<title>Spirograph Art</title>
<style>
body {{
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: radial-gradient(circle at center, #000428, #004e92);
}}
svg {{
  animation: rotate 20s linear infinite;
}}
@keyframes rotate {{
  from {{ transform: rotate(0deg); }}
  to {{ transform: rotate(360deg); }}
}}
path {{
  fill: none;
  stroke: url(#grad);
  stroke-width: 2;
}}
</style>
</head>
<body>
<svg width='500' height='500' viewBox='-250 -250 500 500'>
<defs>
<linearGradient id='grad' gradientTransform='rotate(90)'>
  <stop offset='0%' stop-color='#ff5f6d'/>
  <stop offset='100%' stop-color='#ffc371'/>
</linearGradient>
</defs>
<path d='{path}'/>
</svg>
</body>
</html>"""
    with open("visuals/spirograph.html", "w") as f:
        f.write(html)
    print("Generated visuals/spirograph.html")


if __name__ == "__main__":
    main()
