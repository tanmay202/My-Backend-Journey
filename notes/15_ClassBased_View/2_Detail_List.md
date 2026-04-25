# Django Class-Based Detail View (CBV)

## Introduction

In Django, a **DetailView** is a class-based view used to display **a single object** from the database.

It is part of Django’s built-in generic views and helps reduce boilerplate code compared to function-based views (FBVs).

## Function-Based View Before

    def detail(request, id):
        item = Item.objects.get(pk=id)
        context = {
            'item': item
        }
        return render(request, 'food/detail.html', context)

## Class-Based Detail View After

### Import DetailView

    from django.views.generic.detail import DetailView

### Create the CBV

    class FoodDetail(DetailView):
        model = Item
        template_name = 'food/detail.html'
        context_object_name = 'item'

## Explanation

- `model = Item`  
  Specifies which model to fetch data from.

- `template_name = 'food/detail.html'`  
  Defines which template will render the data.

- `context_object_name = 'item'`  
  The variable name used inside the template.

## URL Configuration

### Before

    path('<int:id>/', views.detail, name='detail')

### After

    path('<int:pk>/', views.FoodDetail.as_view(), name='detail')

## Important Change

In a `DetailView`, the parameter must be `pk` (primary key) instead of `id`.

## Key Concept

| View Type | Purpose |
|----------|--------|
| ListView | Display multiple objects |
| DetailView | Display a single object |

## Summary

- `DetailView` is used to show one object.
- It automatically fetches data using the primary key (`pk`).
- It reduces manual querying and context handling.
- It is cleaner and more maintainable than FBVs.

## Template Example

    <h1>{{ item.item_name }}</h1>
    <img src="{{ item.item_image }}" alt="">
    <p>{{ item.item_description }}</p>

## Conclusion

By switching to **Class-Based DetailView**, we simplify our Django code and follow a more scalable and reusable structure.