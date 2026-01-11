
## 1. Bootstrap Cards

### What is a Card?

A **Card** is a flexible container used to display **content and actions** about a single subject (e.g., product, profile, article).

### When to Use

* Product listings
* User profiles
* Blog previews
* Dashboards

### Example Syntax

```html
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Card Title</h5>
    <p class="card-text">
      This is some text inside a Bootstrap card.
    </p>
    <a href="#" class="btn btn-primary">Read More</a>
  </div>
</div>
```

---

## 2. Bootstrap Accordions

### What is an Accordion?

An **Accordion** is a vertically stacked list of items that can be **expanded or collapsed** to show/hide content.

### When to Use

* FAQs
* Collapsible sections
* Long explanations

### Example Syntax

```html
<div class="accordion" id="exampleAccordion">

  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" data-bs-toggle="collapse" data-bs-target="#itemOne">
        Accordion Item One
      </button>
    </h2>

    <div id="itemOne" class="accordion-collapse collapse show">
      <div class="accordion-body">
        This is the content of the first accordion item.
      </div>
    </div>
  </div>

</div>
```

---

## 3. Bootstrap Alerts

### What is an Alert?

An **Alert** is used to display **important messages** such as success, warning, or error notifications.

### When to Use

* Form feedback
* System messages
* Notifications

### Example Syntax

```html
<div class="alert alert-success" role="alert">
  Your operation was successful!
</div>

<div class="alert alert-danger" role="alert">
  Something went wrong.
</div>
```

---

## 4. Bootstrap Navigation Bars (Navbar)

### What is a Navbar?

A **Navbar** is a responsive navigation header used for **site branding and links**.

### When to Use

* Website header
* Navigation menu
* App navigation

### Example Syntax

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">

    <a class="navbar-brand" href="#">MySite</a>

    <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarMenu">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarMenu">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">About</a>
        </li>
      </ul>
    </div>

  </div>
</nav>
```

---

## 5. Bootstrap Carousels

### What is a Carousel?

A **Carousel** is a slideshow component used to cycle through images or content.

### When to Use

* Image sliders
* Featured content
* Landing pages

### Example Syntax

```html
<div id="exampleCarousel" class="carousel slide" data-bs-ride="carousel">

  <div class="carousel-inner">

    <div class="carousel-item active">
      <img src="image1.jpg" class="d-block w-100" alt="Image 1">
    </div>

    <div class="carousel-item">
      <img src="image2.jpg" class="d-block w-100" alt="Image 2">
    </div>

  </div>

  <button class="carousel-control-prev" data-bs-target="#exampleCarousel" data-bs-slide="prev">
    <span class="carousel-control-prev-icon"></span>
  </button>

  <button class="carousel-control-next" data-bs-target="#exampleCarousel" data-bs-slide="next">
    <span class="carousel-control-next-icon"></span>
  </button>

</div>
```


