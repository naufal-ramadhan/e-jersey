# E-Jersey
---
<br>
Nama    : Muhammad Naufal Ramadhan <br>
NPM     : 2306241700 <br>
Kelas   : D <br>

Link Web : http://muhammad-naufal324-ejersey.pbp.cs.ui.ac.id/
<br>

---
 #### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
  * Karena pada platform, sekarang diperlukan sinkronisasi data secara _real-time_, selain itu biasanya pada sebuah platform semuanya terbagi-bagi dalam beberapa komponen. Contohnya ada _client-side_ dan _server-side_, semisal terdapat dua user yang sedang menggunakan platformnya, dan user pertama melakukan POST request dan kemudian user selanjutnya melakukan GET request, disini diperlukan _data delivery_ sehingga user kedua mendapatkan informasi yang terbaru. Data delivery memungkinkan komponen-komponen seperti _client-side_ dan _server-side_ untuk berkomunikasi sehingga data pada keduanya dapat sinkron secara _real-time_.
<br>

 #### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
  * Menurut saya sendiri, saya lebih memilih JSON. Untuk alasan mengapa JSON lebih populer dibandingkan XML karena dari sintaksnya sendiri JSON lebih mudah dan tidak se-verbose XML, lalu JSON juga merupakan native JavaScript dan JavaScript sendiri sekarang sedang sangat populer dengan framework-frameworknya, ditambah juga dengan kemudahan proses _parsing_ dari JSON itu sendiri dibandingkan dengan XML.
<br>

 #### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
 * Fungsi dari `is_valid()` adalah untuk me-validasi data-data pada form yang akan di proses, semisal tiap fields pada form tidak boleh blank, maka `is_valid()` akan cek tiap field apakah tidak blank, jika blank maka akan return false, dan dapat dihandle lebih lanjut.
<br>

 #### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
 * csrf_token digunakan untuk mengecek bahwa request yang datang benar dari user yang sebenarnya dan tidak di-_intercept_ atau di-_impersonate_ oleh _unauthorized user_. Jika kita tidak mengeimplementasikan csrf_token bisa saja penyerang mengirim request yang dapat mengancam data-data vital, seperti menghapus data vital atau meminta data-data _confidential_.
<br>

 #### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  1) Membuat input form dengan membuat `forms.py` pada project main. dan membuat class sendiri untuk produk yang mengimplementasikan dari class bernama `ModelForm`. Kemudian untuk menerima input dari user dan menambahkan objek dari model, saya membuat template lain hanya untuk menerima input dalam bentuk table, kemudian jika user me-request POST, maka data yang di-input akan divalidasi dan akan di-simpan ke dalam database menggunakan `form.save()`.
  2) Untuk membuat 4 fungsi views untuk melihat object-object dalam bentuk XML dan JSON, perlu membuat views function nya itu sendiri, saya sendiri memberi namanya `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`. Yang akan mereturn object dari database ke dalam bentuk XML atau JSON menggunakan `serializers` dan direspon balik ke user dalam bentuk HTTP menggunakan `HttpResponse`. Untuk kasus view function untuk melihat product berdasarkan id, terdapat parameter tambahan yaitu `id`. Contoh :<br>
  
     ```
     HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
     ```
  3) Setelah itu, saya juga harus membuat url nya masing-masing view function pada `urls.py`, agar dapat di-request oleh user. Untuk kasus pada urls yang dinamis, seperti ketika me-request url dengan id product, diimplementasikan dengan cara menggunakan `<str:id>` pada pola url, disini menyatakan bahwa akan ada terdapat parameter tambahan yang berupa string bernama id yang kemudian akan di proses pada views function. Contoh :<br>

  ```
     path('xml/<str:id>', views.show_xml_by_id, name='show_xml_by_id_url'),
  ```
