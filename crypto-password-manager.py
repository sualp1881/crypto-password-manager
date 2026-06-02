import hashlib
import os

# Şifrelerin kaydedileceği dosya
VAULT_FILE = "vault.txt"

def hash_password(password):
    """Şifreleri güvenli hale getirmek için SHA-256 ile özetler."""
    return hashlib.sha256(password.encode()).hexdigest()

def create_master():
    """İlk açılışta bir ana şifre oluşturur."""
    print("--- KASA KURULUMU ---")
    master = input("Kasanız için güçlü bir Ana Şifre belirleyin: ")
    with open(".master", "w") as f:
        f.write(hash_password(master))
    print("Kasa başarıyla oluşturuldu!\n")

def check_master():
    """Giriş yaparken ana şifreyi kontrol eder."""
    if not os.path.exists(".master"):
        create_master()
        return True
    
    print("--- KASA GİRİŞİ ---")
    attempt = input("Ana Şifrenizi girin: ")
    with open(".master", "r") as f:
        saved_hash = f.read()
    
    if hash_password(attempt) == saved_hash:
        print("Erişim onaylandı! 🔥\n")
        return True
    else:
        print("Hatalı şifre! Erişim reddedildi.")
        return False

def add_password():
    """Kasaya yeni hesap ve şifre ekler."""
    platform = input("Platform adı (Örn: Discord, Steam): ")
    username = input("Kullanıcı adı veya E-posta: ")
    password = input("Şifre: ")
    
    # Basit bir formatla dosyaya yazıyoruz
    with open(VAULT_FILE, "a") as f:
        f.write(f"{platform} | {username} | {password}\n")
    print(f"🎉 {platform} şifresi kasaya güvenle kaydedildi!\n")

def list_passwords():
    """Kasaya kayıtlı şifreleri listeler."""
    if not os.path.exists(VAULT_FILE) or os.stat(VAULT_FILE).st_size == 0:
        print("Kasada henüz kayıtlı şifre yok.\n")
        return
    
    print("--- KAYITLI ŞİFRELERİNİZ ---")
    with open(VAULT_FILE, "r") as f:
        for line in f:
            print(line.strip())
    print("----------------------------\n")

def main():
    if not check_master():
        return

    while True:
        print("1. Yeni Şifre Ekle")
        print("2. Şifreleri Listele")
        print("3. Kasayı Kapat ve Çık")
        secim = input("Yapmak istediğiniz işlemi seçin (1-3): ")
        print()

        if secim == "1":
            add_password()
        elif secim == "2":
            list_passwords()
        elif secim == "3":
            print("Kasa kilitlendi. Güvenle çıkış yapıldı!")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.\n")

if __name__ == "__main__":
    main()
