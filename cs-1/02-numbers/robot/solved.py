stroke_color = input("stroke color (black): ") or "black"
stroke_width = float(input("stroke width (1): ") or 1)
face_fill = input("face fill (none): ") or "none"
brow_offset = float(input("brow offset (-2): ") or -2)
eye_radius = float(input("eye radius (5): ") or 5)
eye_fill = input("eye fill (none): ") or "none"
nose_width = float(input("nose width (10): ") or 10)
nose_height = float(input("nose height (10): ") or 10)
nose_fill = input("nose fill (none): ") or "none"
mouth_rx = float(input("mouth radius x (10): ") or 10)
mouth_ry = float(input("mouth radius y (2): ") or 2)
mouth_fill = input("mouth fill (none): ") or "none"

svg = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="-50 -50 100 100"
  width="100mm"
  height="100mm"
>
  <g stroke-width="{stroke_width}" stroke="{stroke_color}">
    <rect
      width="80"
      height="60"
      x="-40"
      y="-30"
      fill="{face_fill}"
    />

    <line
      x1="-25"
      y1="-20"
      x2="-15"
      y2="{-20 + brow_offset}"
    />

    <line
      x1="25"
      y1="-20"
      x2="15"
      y2="{-20 + brow_offset}"
    />

    <circle
      cx="-20"
      cy="-5"
      r="{eye_radius}"
      fill="{eye_fill}"
    />

    <circle
      cx="20"
      cy="-5"
      r="{eye_radius}"
      fill="{eye_fill}"
    />

    <path
      d="M 0 0 l {nose_width / 2} {nose_height} h -{nose_width} z"
      fill="{nose_fill}"
    />

    <ellipse
      cx="0"
      cy="22"
      rx="{mouth_rx}"
      ry="{mouth_ry}"
      fill="{mouth_fill}"
    />
  </g>
</svg>
"""

with open("face.svg", "w") as file:
    file.write(svg)
