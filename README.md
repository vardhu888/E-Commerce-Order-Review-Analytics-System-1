<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>E-Commerce Order & Review Analytics System</title>
<style>
body{
    font-family: Arial, sans-serif;
    margin:40px;
    line-height:1.6;
}
h1,h2{
    color:#2c3e50;
}
code{
    background:#f4f4f4;
    padding:3px 6px;
    border-radius:4px;
}
.section{
    margin-bottom:30px;
}
</style>
</head>

<body>

<h1>E-Commerce Order & Review Analytics System</h1>

<p>
This is a <b>menu-driven Python application</b> that simulates a simple 
E-Commerce order management system. The program allows users to view a product 
catalog, place orders, analyze order data, and store reports in a file.
</p>

<div class="section">
<h2>Features</h2>
<ul>
<li>Display product catalog with price and stock information</li>
<li>Place orders with input validation</li>
<li>Automatic stock update after each order</li>
<li>Discount applied for orders above ₹10,000</li>
<li>Customer rating system for products</li>
<li>Analytics summary including:
    <ul>
        <li>Total revenue</li>
        <li>Most frequently ordered product</li>
        <li>Highest rated product</li>
        <li>Average rating per product</li>
    </ul>
</li>
<li>Save order reports to a text file</li>
</ul>
</div>

<div class="section">
<h2>Technologies Used</h2>
<ul>
<li>Python</li>
<li>Dictionaries</li>
<li>Tuples</li>
<li>Lists</li>
<li>Exception Handling</li>
<li>File Handling</li>
<li>Math Module</li>
</ul>
</div>

<div class="section">
<h2>Program Functions</h2>
<ul>
<li><b>display_catalog()</b> – Displays available products</li>
<li><b>place_order()</b> – Allows users to place orders and provide ratings</li>
<li><b>analytics_summary()</b> – Generates order analytics</li>
<li><b>save_report()</b> – Saves order details to a file</li>
</ul>
</div>

<div class="section">
<h2>How to Run</h2>
<ol>
<li>Install Python on your system</li>
<li>Download or clone this repository</li>
<li>Run the program using:</li>
</ol>

<pre><code>python ecommerce_system.py</code></pre>

</div>

<div class="section">
<h2>Menu Options</h2>
<ul>
<li>1 – Display Product Catalog</li>
<li>2 – Place Order</li>
<li>3 – View Analytics Summary</li>
<li>4 – Save Order Report to File</li>
<li>5 – Exit Program</li>
</ul>
</div>

<div class="section">
<h2>Output File</h2>
<p>
The program stores order information in a file named 
<b>orders_report.txt</b>.
</p>
</div>

<div class="section">
<h2>Author</h2>
<p>
Developed by <b>Vardhu</b>
</p>
</div>

</body>
</html>
