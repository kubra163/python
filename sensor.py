import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

seri_port = "COM7"  # Arduino'nun bağlı olduğu port
baud_hizi = 9600

ser = serial.Serial(seri_port, baud_hizi, timeout=1)

x_data = []
y_data = []

fig, ax = plt.subplots()
line, = ax.plot([], [], 'b-o', label="Mesafe (cm)")
ax.set_ylim(0, 220)  # Mesafe aralığı
ax.set_xlim(0, 50)
ax.set_xlabel("Ölçüm Sayısı")
ax.set_ylabel("Mesafe (cm)")
ax.legend()

def animate(i):
    if ser.in_waiting > 0:
        try:
            veri = ser.readline().decode(errors='ignore').strip()
            if not veri:
                return line,
            parts = veri.split(",")
            if len(parts)<2:
                return line,
            mesafe = int(parts[0])
            led = int(parts[1])

            x_data.append(len(x_data))
            y_data.append(mesafe)
            if len(x_data)>50:
                x_data = x_data[-50:]
                y_data = y_data[-50:]

            ax.set_xlim(max(0, x_data[0]), x_data[-1]+1)
            line.set_data(x_data, y_data)
            ax.set_title(f"Mesafe: {mesafe} cm    LED Kademesi: {led}/5")
        except:
            pass
    return line,

ani = FuncAnimation(fig, animate, interval=100)
plt.tight_layout()
plt.show()

