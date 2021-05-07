# Membandingkan Metode / Cara Iterasi

Metode / cara coding programmer dalam looping/iterasi bisa berbagai macam. 
Tidak ada yang salah dengan metode-metode ini karena hasilnya sama. 
Namun perbedaan ini akan mempengaruhi performance. Misal:

    data = [['ezncn', 2160501], 
        ['tpblq', 8963617], 
        ['xdvaf', 138208], 
        ['qulpc', 3878119], 
        ...,
        ]

Kita ingin retrieve data di atas untuk mendapatkan data_copy sbb:

    data_copy = [ 2160501, 8963617, 138208, 3878119, ... ]

Beberapa metode / caranya untuk mendapatkan hasil yang sama 
(tanpa import modul yang lain) adalah sbb:

## Metode 1

    data_copy = []
    for i in range(len(data)):
        data_copy.append(data[i][1])

## Metode Dua

    data_copy = []
    for d in data:
        data_copy.append(d[1])

## Metode Tiga

    data_copy = [ data[i][1] for i in range(len(data)) ]

## Metode Empat

    data_copy = [ d[1] for d in data ]

## Hasil

Saya baru menemukan 4 metode yang dapat saya rangkum.
Barangkali teman ada lagi metode lain? 

Dari ke-empat metode tersebut, saya hitung waktu yang dibutuhkan 
menggunakan script python dg fitur:
    
   * Banyaknya trial digenerate secara acak 1 s.d 10
   * Banyaknya data digenerate secara acak 1ribu sd 900ribu per trial
   * Urutan memproses metode dilakukan acak per trial
   
Penampakan hasil salah satu output yg dijalankan pada notebook i5 saya sbb:

    ## Hasil Rekap Waktu (seconds) dan Speed
    Metode Dua   = 0.164624 *************        1.5x
    Metode Tiga  = 0.193826 ***************      1.3x
    Metode Satu  = 0.247912 ******************** 1.0x
    Metode Empat = 0.100872 ********             2.5x
    Banyaknya data: 10780000
    Banyaknya trial: 7 

## Kesimpulan

* Ternyata kecepatan Metode Empat 2.5x dari Metode Satu. 
* Diikuti Metode Dua dg kecepatan 1.5x Metode Satu.

tags: #sharing #tips
