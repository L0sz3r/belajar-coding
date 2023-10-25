from cryptography.fernet import Fernet
import base64

# Masukkan pesan yang dienkripsi dan kunci yang digunakan
encrypted_message = "gAAAAABkzWGSzE6VQNTzvRXOXekQeW4CY6NiRkzeImo9LuYBHAYw_hagTJLJL0c-kmNsjY33IUbU2IWlqxA3Fpp9S7RxNkiwMDZgLmRlI9-lGAEW-_i72RSDvylNR3QkpJW2JxubjLUC5VwoVgH62wxDuYu1rRD5KadwTADdABqsx2MkY6fKNTMCYY09Se6yjtRBftfTJUL-LKz2bwgXNd6O-WpbfXEMvCv3gNQ7sW4pgUnb-gDVZvrLNrug_1YFaIe3yKr0Awo0HIN3XMdZYpSE1c9P4G0sMQ=="
key = "correctstaplecorrectstaplecorrec"

# Konversi kunci ke format base64 yang sesuai
key = base64.urlsafe_b64encode(key.encode())

# Konversi kunci menjadi objek Fernet
fernet_key = Fernet(key)

# Dekripsi pesan
decrypted_message = fernet_key.decrypt(encrypted_message.encode())

# Tampilkan pesan yang telah didekripsi
print("Pesan yang didekripsi:", decrypted_message.decode())
