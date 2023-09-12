# **Link website: **

## Cara saya mengimplementasikan _checklist - checklist_ di ketentuan tugas: 

## Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

## Apakah itu MVC, MVT, MVVM dan apa perbedaan dari ketiganya?
MVC (Model-View-Controller):

Model: Mewakili data dan logika bisnis aplikasi. Ini adalah bagian yang bertanggung jawab untuk mengelola dan memanipulasi data.
View: Menampilkan informasi kepada pengguna dan menanggapi input pengguna. Ini adalah bagian yang berhubungan dengan tampilan atau antarmuka pengguna.
Controller: Bertindak sebagai perantara antara Model dan View. Mengatur alur kontrol aplikasi, menerima input dari pengguna, dan mengubah Model atau View sesuai dengan instruksi.
Perbedaan utama: Dalam MVC, Controller adalah komponen yang mengendalikan alur logika aplikasi, sedangkan Model dan View berinteraksi melalui Controller. MVC sering digunakan dalam pengembangan web dan desktop.

MVT (Model-View-Template):

Model: Sama seperti dalam MVC, Model adalah komponen yang mengelola data dan logika bisnis.
View: Ini adalah komponen yang menangani tampilan atau antarmuka pengguna, seperti dalam MVC.
Template: Template mengatur cara data dari Model akan ditampilkan dalam View. Template ini biasanya terkait dengan teknologi server-side rendering seperti dalam framework Django (Python).
Perbedaan utama: MVT adalah variasi dari MVC yang umumnya digunakan dalam konteks aplikasi web yang menggunakan server-side rendering. Perbedaan utama adalah penggunaan Template yang mengatur tampilan.

MVVM (Model-View-ViewModel):

Model: Sama seperti dalam MVC dan MVT, Model mengelola data dan logika bisnis.
View: Ini adalah komponen yang menangani tampilan atau antarmuka pengguna, seperti dalam MVC dan MVT.
ViewModel: ViewModel adalah lapisan tambahan yang berfungsi sebagai perantara antara Model dan View. Ini mengubah data dari Model menjadi format yang dapat ditampilkan di View dan merespons perubahan di View dengan mengupdate Model.
Perbedaan utama: MVVM adalah arsitektur yang umumnya digunakan dalam pengembangan aplikasi berbasis platform seperti Xamarin (untuk pengembangan aplikasi seluler) atau dalam aplikasi berbasis framework seperti AngularJS (untuk pengembangan web). ViewModel adalah komponen unik yang membedakannya dari MVC dan MVT, dan tujuannya adalah memisahkan logika tampilan dari Model dan menghubungkannya dengan View.
