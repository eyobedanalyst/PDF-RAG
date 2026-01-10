# **📘 BOOTSTRAP COMPLETE STUDY NOTE**

*(Based on everything we discussed, with examples)*

---

## **PAGE 1: What is Bootstrap?**

### **Definition (Simple)**

**Bootstrap** is a **CSS framework** that helps you build **responsive, mobile-friendly websites faster**.

Instead of writing a lot of CSS yourself, Bootstrap gives you **ready-made classes**.

---

### **Why Bootstrap is Important**

* Saves time

* Works on phones, tablets, and desktops

* Consistent design

* Easy to learn

* Used in real websites

---

### **Bootstrap Uses:**

* Layout (Grid system)

* Typography

* Buttons

* Navigation bars

* Cards

* Tables

* Alerts

* Badges

* Accordions

* Carousels

---

### **How to Include Bootstrap**

\<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"\>  
\<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"\>\</script\>

---

## **PAGE 2: Bootstrap Grid System (Core Concept)**

### **Grid Structure**

Bootstrap layout always follows this order:

container → row → column → content

---

### **Example**

\<div class="container"\>  
  \<div class="row"\>  
    \<div class="col-6"\>Left\</div\>  
    \<div class="col-6"\>Right\</div\>  
  \</div\>  
\</div\>

---

### **Columns Explained**

* Bootstrap grid has **12 columns**

* You divide space using col-\*

Examples:

* col-6 → half width

* col-4 → one third

* col-3 → one quarter

---

### **Responsive Columns**

\<div class="col-12 col-md-6 col-lg-4"\>Content\</div\>

Meaning:

* Mobile: full width

* Tablet: half

* Desktop: one third

---

## **PAGE 3: Gutters, Rows & Column Breaks**

### **Gutters (Space between columns)**

\<div class="row g-3"\>

* g-0 → no space

* g-3 → medium space

* g-5 → large space

---

### **No Gutters Example**

\<div class="row g-0"\>  
  \<div class="col-6 bg-primary"\>A\</div\>  
  \<div class="col-6 bg-success"\>B\</div\>  
\</div\>

---

### **Column Break (Force New Line)**

\<div class="w-100"\>\</div\>

This forces columns to **wrap to the next line**.

---

### **Responsive Column Break**

\<div class="w-100 d-none d-md-block"\>\</div\>

Meaning:

* Hidden on small screens

* Breaks line on medium+ screens

---

## **PAGE 4: Alignment (Horizontal & Vertical)**

### **Horizontal Alignment**

\<div class="row justify-content-center"\>

Options:

* justify-content-start

* justify-content-center

* justify-content-end

* justify-content-between

---

### **Vertical Alignment**

\<div class="row align-items-center"\>

Options:

* align-items-start

* align-items-center

* align-items-end

---

### **Example**

\<div class="row align-items-center justify-content-center" style="height:200px"\>  
  \<div class="col-4 bg-warning text-center"\>Centered\</div\>  
\</div\>

---

## **PAGE 5: Reordering & Offsetting Columns**

### **Order Classes**

\<div class="col order-2"\>Second\</div\>  
\<div class="col order-1"\>First\</div\>

Meaning:

* Visual order changes

* HTML order stays the same

---

### **Responsive Order**

\<div class="col order-1 order-md-2"\>Box\</div\>

---

### **Offset Classes**

\<div class="col-md-4 offset-md-4"\>

This moves the column **to the right**.

---

### **Margin Utilities**

\<div class="ms-auto"\>

* Pushes content to the **right**

* Used often in navbars

---

## **PAGE 6: Typography (Text Styling)**

### **Headings**

Bootstrap styles \<h1\> to \<h6\> automatically.

---

### **Display Headings**

\<h1 class="display-4"\>Big Title\</h1\>

---

### **Lead Paragraph**

\<p class="lead"\>  
  This paragraph stands out.  
\</p\>

---

### **Text Alignment**

\<p class="text-center"\>Center\</p\>  
\<p class="text-end"\>Right\</p\>

---

### **Text Colors**

\<p class="text-primary"\>Blue\</p\>  
\<p class="text-danger"\>Red\</p\>

---

### **Text Transform**

\<p class="text-uppercase"\>uppercase\</p\>  
\<p class="text-capitalize"\>capitalize words\</p\>

---

## **PAGE 7: Lists, Images, Figures & Blockquotes**

### **Lists**

\<ul class="list-group"\>  
  \<li class="list-group-item"\>Item 1\</li\>  
  \<li class="list-group-item"\>Item 2\</li\>  
\</ul\>

---

### **Images**

\<img src="img.jpg" class="img-thumbnail"\>  
\<img src="img.jpg" class="rounded"\>

---

### **Aligning Images**

\<img src="img.jpg" class="float-start"\>  
\<img src="img.jpg" class="float-end"\>

---

### **Figure**

\<figure class="figure"\>  
  \<img src="img.jpg" class="figure-img img-fluid rounded"\>  
  \<figcaption class="figure-caption"\>Caption\</figcaption\>  
\</figure\>

---

### **Blockquote**

\<blockquote class="blockquote"\>  
  \<p\>Education is the key.\</p\>  
  \<footer class="blockquote-footer"\>Nelson Mandela\</footer\>  
\</blockquote\>

---

## **PAGE 8: Tables**

### **Basic Table**

\<table class="table"\>

---

### **Styled Table**

\<table class="table table-striped table-bordered"\>

---

### **Contextual Colors**

\<tr class="table-success"\>\</tr\>  
\<tr class="table-danger"\>\</tr\>

---

### **Responsive Table**

\<div class="table-responsive"\>  
  \<table class="table"\>\</table\>  
\</div\>

---

## **PAGE 9: Components (Alerts, Badges, Accordion)**

### **Alerts**

\<div class="alert alert-success"\>  
  Success message  
\</div\>

---

### **Badges (Simple Meaning)**

Badges show **small extra info** like counts or status.

\<span class="badge bg-danger"\>New\</span\>

---

### **Badge with Button**

\<button class="btn btn-primary"\>  
  Messages \<span class="badge bg-light text-dark"\>3\</span\>  
\</button\>

---

### **Accordion (FAQ Style)**

\<div class="accordion"\>  
  \<div class="accordion-item"\>  
    \<button class="accordion-button" data-bs-toggle="collapse" data-bs-target="\#a1"\>  
      Question  
    \</button\>  
    \<div id="a1" class="accordion-collapse collapse show"\>  
      \<div class="accordion-body"\>Answer\</div\>  
    \</div\>  
  \</div\>  
\</div\>

---

## **PAGE 10: Navbar & Carousel (Real Websites)**

### **Navbar**

\<nav class="navbar navbar-expand-lg navbar-dark bg-primary"\>  
  \<div class="container-fluid"\>  
    \<a class="navbar-brand"\>MySite\</a\>

    \<button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="\#nav"\>  
      \<span class="navbar-toggler-icon"\>\</span\>  
    \</button\>

    \<div class="collapse navbar-collapse" id="nav"\>  
      \<ul class="navbar-nav ms-auto"\>  
        \<li class="nav-item"\>\<a class="nav-link"\>Home\</a\>\</li\>  
        \<li class="nav-item"\>\<a class="nav-link"\>About\</a\>\</li\>  
      \</ul\>  
    \</div\>  
  \</div\>  
\</nav\>

---

### **Carousel**

\<div id="carousel" class="carousel slide" data-bs-ride="carousel"\>  
  \<div class="carousel-inner"\>  
    \<div class="carousel-item active"\>  
      \<img src="img1.jpg" class="d-block w-100"\>  
    \</div\>  
    \<div class="carousel-item"\>  
      \<img src="img2.jpg" class="d-block w-100"\>  
    \</div\>  
  \</div\>  
\</div\>

---

## **✅ FINAL SUMMARY (EXAM READY)**

* Bootstrap \= responsive CSS framework

* Grid \= container → row → col

* 12-column system

* Gutters control spacing

* Order & offset control layout flow

* Typography styles text

* Tables, badges, alerts show data

* Navbar & carousel need **Bootstrap JS**

