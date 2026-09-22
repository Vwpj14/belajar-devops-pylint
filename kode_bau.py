"""Modul contoh untuk demonstrasi perbaikan kode sesuai PEP 8."""


def hitung_operasi(kondisi, nilai_list, nilai_tambahan):
    """Menghitung operasi sederhana dari beberapa nilai input.

    Args:
        kondisi: Tuple berisi (nilai_a, nilai_b, nilai_c) untuk pengecekan.
        nilai_list: List berisi nilai yang elemen pertamanya digunakan.
        nilai_tambahan: Nilai integer tambahan untuk penjumlahan.

    Returns:
        Hasil penjumlahan nilai_list[0], nilai_tambahan, dan konstanta
        lokal, atau None jika kondisi tidak terpenuhi.
    """
    nilai_a, nilai_b, nilai_c = kondisi
    konstanta_l = 1
    konstanta_o = 0

    if nilai_a and not nilai_b and nilai_c is None:
        try:
            hasil = nilai_list[0] + nilai_tambahan + konstanta_l + konstanta_o
            print(hasil)
            return hasil
        except (IndexError, TypeError):
            return None
    return None


def main():
    """Fungsi utama program."""
    hitung_operasi((True, False, None), [2], 3)


if __name__ == "__main__":
    main()
