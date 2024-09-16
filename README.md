# E-Jersey
---
<br>
Nama    : Muhammad Naufal Ramadhan <br>
NPM     : 2306241700 <br>
Kelas   : D <br>

Link Web : http://muhammad-naufal324-ejersey.pbp.cs.ui.ac.id/
<br>

---
# Tugas 2

#### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 1) Langkah Pertama yaitu me-setup. Pertama, membuat repository baru di Github, kemudian Clone ke Local. Setelah inisialisasi github selesai, tambahkan gitignore dan lain-lain, di dalam dir git, saya inisiasi virtual environment untuk project tersebut, kemudian saya menginstall semua dependency yang diperlukan pada virtual environment nya, seperti django.
 2) Pada tahap ini, saya membuat project E-jersey saya dan membuat app dalam project tersebut bernama main, dengan menjalankan `django-admin startproject e_jersey .` untuk membuat project, dan `python manage.py startapp main` untuk membuat aplikasi bernama main.
 3) Setelah ini selesai, saya me_include_ aplikasi dan url main saya pada settings.py dan urls.py di dir project, setelah itu juga menambahkan url pada url di level aplikasi main, sehingga django bisa mehandle pola url yang akan diberikan.
 4) Selanjutnya membuat model dengan bernama Product, inisialisasi dilakukan pada models.py, field yang saya berikan pada Product saya meliputi, nama, harga, description, club, type, dan slug.
 5) Lalu, saya membuat beberapa template HTML yang akan saya tampilkan pada user, template-template saya simpan di directory template didalam directory main.
 6) Selanjutnya saya membuat beberapa fungsi pada views, untuk menghandle beberapa pola url yang diterima, sehingga views dapat menentukan template apa yang akan dipakai dan data apa saja yang perlu difetch agar bisa sampai pada user dalam bentuk yang komplet.
 7) Setelah semua selesai, saya membuat project baru pada website pws. Sehingga git saya memiliki dua remote, yaitu remote origin dan remote pws. Selanjutnya saya push ke dua remote tersebut, sehingga pws dapat me_build_ project saya dan dideploy, sehingga teman-teman saya dapat melihat web saya dari komputernya masing-masing.
 8) Selanjutnya saya membuat README.md pada github saya untuk menjawab beberapa pertanyaan seperti yang saya lakukan pada saat saya mengetik sekarang. 
<br>

#### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. 
<br>

  ![Bagan](images/tugas02/uml.png)
  <br>
  
  1. Pertama, User akan melakukan HTTP request yang kemudian akan di handle oleh View. Untuk menentukan apa yang direquest dan apa yang akan di respon balik, akan ditentukan di dalam urls.py. Berdasarkan pattern url yang direquest, akan menentukan function View apa yang akan dijalankan didalam Views.py.
  2. View me-request data yang diperlukan untuk ditampilkan kepada user, data-data yang diperlukan sudah tercantum didalam function view yang dijalankan, dan akan _Get_ data field yang tersedia didalam models.py.
  3. View akan me-request HTML apa yang dipopulasikan dengan data pada Template, untuk menentukan berkas HTML yang mana akan di-request sudah ditentukan di dalam function View. Lalu setelah dapat berkas HTML yang di-request kemudian akan direspon balik ke User dengan HTML yang sudah dipopulasikan dengan data dalam bentuk HTTP.
<br>

#### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
  *  Git mempunyai beberapa peran penting dalam pengembangan perangkat lunak, diantaranya :
    <br>
      1. Version Control
          * Dengan git, semisal kita melakukan pengembangan aplikasi berkala, dengan adanya git yang berperan sebagai version control, kita dapat melihat dan membandingkan perubahan apa saja dibandingkan versi aplikasi yang sebelumnya. Selain itu, jika aplikasi kita terdapat bug atau error semacamnya dan tidak bisa di-fix, kita dapat me-_rollback_ aplikasi kita pada versi sebelumnya.
      2. Platform Kolaborasi
          * Dengan git memungkinkan untuk beberapa developer untuk berkolaborasi untuk mengembangkan sebuah aplikasi. Git me-support _branching_ dan _merging_, sehingga memungkinkan untuk beberapa developer untuk mengerjakan fitur aplikasi masing-masing pada _branch_ yang sudah ditentukan, dan jika sudah selesai dapat di _merge_ ke dalam branch utama.
      3. Backup
          * Dengan menggunakan git, automatis kita me-_upload_ code kita ke-_cloud_, dengan server git yang sudah terdistribusi di berbagai belahan dunia. Sehingga jika kita kehilangan komputer fisik kita, kode kita masih tersimpan di server git.
<br>

#### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  * Menurut saya, Django sendiri memiliki konsep yang jelas dengan model MVT itu sendiri. Selain itu, bahasa utama yang digunakan juga python, bahasa yang menurut saya lebih _straight-forward_ dan tidak menggunakan begitu banyak simbol-simbol dibandingkan dengan bahasa lain. Ditambah dengan banyaknya dokumentasi yang tersedia, komunitas yang luas, dan sudah banyak _built-in-feature_ yang tersedia.
<br>

#### 5. Mengapa model pada Django disebut sebagai ORM?
  * ORM itu sendiri memiliki arti Object-Related-Mapping, atau sebuah teknik untuk me-_convert_ sebuah object menjadi object pada sistem lain. dan Models pada django dapat disebut sebagai ORM, karena django memiliki peran sebagai _interface_ diantara Object pada Python dengan table pada sql. Pada Django, kita tidak perlu ber-urusan dengan sql, kita bisa langsung add, update, delete database langsung dengan python.

# Tugas 3

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

### Screenshot pada Postman
# XML
 ![XML](images/tugas03/xml.png)
 # JSON
 ![JSON](images/tugas03/json.png)
 # XML_ID
 ![XML_ID](images/tugas03/xml_id.png)
 # JSON_ID
 ![JSON_ID](images/tugas03/json_id.png)
