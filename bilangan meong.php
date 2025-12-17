<!DOCTYPE html>
    <meta charset="UTF-8">

    <form method="post">
        <title>Cek Bilangan Positif, Negatif, dan Prima</title>
        <h1>Cek Bilangan Positif, Negatif, dan Prima</h1>
        Masukkan bilangan: <input type="number" name="bilangan" required>
        <input type="submit" value="Cek">
    </form>

<?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") { //Memastikan kode PHP berjalan setelah klik tombol CEK
        $bilangan = intval($_POST['bilangan']); //Pengubah nilai menjadi integer atau bilangan bulat
    
        if ($bilangan > 0) {
            echo "Bilangan Positif<br>";
        } else if ($bilangan < 0) {
            echo "Bilangan Negatif<br>";
        } else {
            echo "Bilangan Nol<br>";
        }
    
        if ($bilangan > 1) {
            $prima = true;
        for ($i = 2; $i <= ($bilangan-1); $i++) {
        if ($bilangan % $i == 0) {
            $prima = false;
            break;
            }
        }
            echo $prima ? "Bilangan Prima" : "Bilangan Bukan Prima";
        } else {
            echo "Bilangan Bukan Prima";
        }
    }
?>