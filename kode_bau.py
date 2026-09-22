"""Modul contoh untuk demonstrasi perbaikan kode sesuai PEP 8."""


def hitung_operasi(nilai_a, nilai_b, nilai_c, nilai_d, nilai_e, nilai_f):
    """Menghitung operasi sederhana dari beberapa nilai input.

    Args:
        nilai_a: Nilai boolean pertama.
        nilai_b: Nilai boolean kedua.
        nilai_c: Nilai opsional ketiga.
        nilai_d: Nilai integer keempat.
        nilai_e: List berisi nilai kelima.
        nilai_f: Nilai integer keenam.

    Returns:
        Hasil penjumlahan nilai_e[0], nilai_f, dan konstanta lokal,
        atau None jika kondisi tidak terpenuhi.
    """
    konstanta_l = 1
    konstanta_o = 0

    if nilai_a and not nilai_b and nilai_c is None:
        try:
            hasil = nilai_e[0] + nilai_f + konstanta_l + konstanta_o
            print(hasil)
            return hasil
        except (IndexError, TypeError):
            return None
    return None


def main():
    """Fungsi utama program."""
    hitung_operasi(True, False, None, 1, [2], 3)


if __name__ == "__main__":
    main()
