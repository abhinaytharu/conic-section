# Conic Sections: Comprehensive Anatomy and Properties
import numpy as np
import matplotlib.pyplot as plt

# --- PARAMETERS ---
p_para = 2           # Parabola: p = focal distance
a_ell, b_ell = 5, 3  # Ellipse: a = semi-major, b = semi-minor
a_hyp, b_hyp = 3, 2  # Hyperbola: a = semi-transverse, b = semi-conjugate

# Create Figure
plt.style.use('dark_background')
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 7))

# --- PARABOLA ANATOMY (y = x²/4p) ---
x_p = np.linspace(-10, 10, 400); y_p = x_p**2 / (4 * p_para)
ax1.plot(x_p, y_p, color='#00d1ff', linewidth=3)
ax1.scatter(0, p_para, color='#ff3366', s=100, label='Focus (F)')
ax1.scatter(0, 0, color='#ffffff', s=100, label='Vertex (V)')
ax1.axhline(-p_para, color='#ffcc00', linestyle='--', label='Directrix')
# Label p
ax1.annotate('', xy=(0, p_para), xytext=(0, 0), arrowprops=dict(arrowstyle='<->', color='#ffffff'))
ax1.text(0.2, p_para/2, 'p', color='#ffffff', fontsize=12, fontweight='bold')
# General Equation
info_p = "Eq: y = x² / 4p\np: dist(Vertex, Focus)\nDirectrix: y = -p"
ax1.text(-9, 8, info_p, color='white', bbox=dict(facecolor='#00d1ff', alpha=0.2, boxstyle='round,pad=0.5'))
ax1.set_title("Parabola Anatomy", color='#00d1ff', fontsize=14, pad=15)
ax1.set_xlim(-10, 10); ax1.set_ylim(-3, 10); ax1.set_aspect('equal'); ax1.grid(alpha=0.1)

# --- ELLIPSE ANATOMY (x²/a² + y²/b² = 1) ---
t = np.linspace(0, 2*np.pi, 400); x_e = a_ell * np.cos(t); y_e = b_ell * np.sin(t)
ax2.plot(x_e, y_e, color='#ff0077', linewidth=3)
# Major/Minor Axes
ax2.plot([-a_ell, a_ell], [0, 0], color='#00d1ff', linewidth=2, linestyle='--', label='Major Axis (2a)')
ax2.plot([0, 0], [-b_ell, b_ell], color='#ffcc00', linewidth=2, linestyle='--', label='Minor Axis (2b)')
# Label a and b
ax2.text(a_ell/2, 0.2, 'a', color='#00d1ff', fontsize=12, fontweight='bold')
ax2.text(0.2, b_ell/2, 'b', color='#ffcc00', fontsize=12, fontweight='bold')
# General Equation & Terms
info_e = "Eq: x²/a² + y²/b² = 1\nMajor Axis: 2a\nMinor Axis: 2b\na: Semi-Major Axis\nb: Semi-Minor Axis"
ax2.text(-6.5, -4.5, info_e, color='white', bbox=dict(facecolor='#ff0077', alpha=0.2, boxstyle='round,pad=0.5'))
ax2.set_title("Ellipse Anatomy", color='#ff0077', fontsize=14, pad=15)
ax2.set_xlim(-7, 7); ax2.set_ylim(-5, 5); ax2.set_aspect('equal'); ax2.grid(alpha=0.1)

# --- HYPERBOLA ANATOMY (x²/a² - y²/b² = 1) ---
x_h_r = np.linspace(a_hyp, 10, 400); y_h_r = b_hyp * np.sqrt(x_h_r**2 / a_hyp**2 - 1)
x_h_l = np.linspace(-10, -a_hyp, 400); y_h_l = b_hyp * np.sqrt(x_h_l**2 / a_hyp**2 - 1)
ax3.plot(x_h_r, y_h_r, color='#a200ff', linewidth=3); ax3.plot(x_h_r, -y_h_r, color='#a200ff', linewidth=3)
ax3.plot(x_h_l, y_h_l, color='#a200ff', linewidth=3); ax3.plot(x_h_l, -y_h_l, color='#a200ff', linewidth=3)
# Transverse/Conjugate Axes
ax3.plot([-a_hyp, a_hyp], [0, 0], color='#00d1ff', linewidth=2, linestyle='--', label='Transverse Axis (2a)')
ax3.plot([0, 0], [-b_hyp, b_hyp], color='#ffcc00', linewidth=2, linestyle='--', label='Conjugate Axis (2b)')
# Label a and b
ax3.text(a_hyp/2, 0.2, 'a', color='#00d1ff', fontsize=12, fontweight='bold')
ax3.text(0.2, b_hyp/2, 'b', color='#ffcc00', fontsize=12, fontweight='bold')
# General Equation & Terms
info_h = "Eq: x²/a² - y²/b² = 1\nTransverse Axis: 2a\nConjugate Axis: 2b\na: Semi-Transverse\nb: Semi-Conjugate"
ax3.text(-9, 5, info_h, color='white', bbox=dict(facecolor='#a200ff', alpha=0.2, boxstyle='round,pad=0.5'))
ax3.set_title("Hyperbola Anatomy", color='#a200ff', fontsize=14, pad=15)
ax3.set_xlim(-10, 10); ax3.set_ylim(-6, 7); ax3.set_aspect('equal'); ax3.grid(alpha=0.1)

plt.tight_layout()
plt.show()
