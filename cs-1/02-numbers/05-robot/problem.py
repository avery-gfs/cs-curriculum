stroke_color = input("stroke color (black): ") or "black"
stroke_width = float(input("stroke width (1): ") or 1)
# face_fill = ??
# brow_offset = ??
# eye_radius = ??
# eye_fill = ??
# nose_width = ??
# nose_height = ??
# nose_fill = ??
# mouth_rx = ??
# mouth_ry = ??
# mouth_fill = ??

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
      fill="none"
    />

    <line
      x1="-25"
      y1="-20"
      x2="-15"
      y2="-22.0"
    />

    <line
      x1="25"
      y1="-20"
      x2="15"
      y2="-22.0"
    />

    <circle
      cx="-20"
      cy="-5"
      r="5.0"
      fill="none"
    />

    <circle
      cx="20"
      cy="-5"
      r="5.0"
      fill="none"
    />

    <path
      d="M 0 0 l 5.0 10.0 h -10.0 z"
      fill="none"
    />

    <ellipse
      cx="0"
      cy="22"
      rx="10.0"
      ry="2.0"
      fill="none"
    />
  </g>
</svg>
"""

with open("face.svg", "w") as file:
    file.write(svg)
