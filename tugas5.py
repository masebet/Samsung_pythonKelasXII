import math # Mengimpor modul math untuk menggunakan konstanta pi

def hitung_volume_bola(jari_jari):
  """
  Menghitung volume bola berdasarkan jari-jarinya.

  Args:
    jari_jari (float): Jari-jari bola.

  Returns:
    float: Volume bola.
  """
  if jari_jari < 0:
    return "Jari-jari tidak boleh negatif" # Menangani input yang tidak valid
  
  # Rumus volume bola: V = (4/3) * π * r³
  volume = (4/3) * math.pi * (jari_jari ** 3)
  return volume

# Contoh penggunaan fungsi
jari_jari_input = 7 # Jari-jari bola
volume_hasil = hitung_volume_bola(jari_jari_input)

print(f"Jari-jari bola: {jari_jari_input}")
print(f"Volume bola adalah: {volume_hasil}")

# Contoh lain
jari_jari_input_lain = 10
volume_hasil_lain = hitung_volume_bola(jari_jari_input_lain)
print(f"\nJari-jari bola: {jari_jari_input_lain}")
print(f"Volume bola adalah: {volume_hasil_lain}")