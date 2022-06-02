from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('foods/', views.FoodList.as_view(), name="food_list"),
    path('foods/new/', views.FoodCreate.as_view(), name="food_create"),
    path('foods/<int:pk>/', views.FoodDetail.as_view(), name="food_detail"),
    path('foods/<int:pk>/update',views.FoodUpdate.as_view(), name="food_update"),
    path('foods/<int:pk>/delete',views.FoodDelete.as_view(), name="food_delete"),
    path('recipes/', views.RecipeList.as_view(), name="recipe_list"),
    path('recipes/new', views.RecipeCreate.as_view(), name="recipe_create"),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('recipes/<int:pk>/update',views.RecipeUpdate.as_view(), name="recipe_update"),
    path('recipes/<int:pk>/delete',views.RecipeDelete.as_view(), name="recipe_delete"),
    path('recipes/<int:pk>/foods/<int:food_pk>/', views.RecipeFoodAssoc.as_view(), name="recipe_food_assoc"),
    path('cookbooks/', views.CookbookList.as_view(), name="cookbook_list"),
    path('cookbooks/new/', views.CookbookCreate.as_view(), name="cookbook_create"),
    path('cookbooks/<int:pk>/', views.CookbookDetail.as_view(), name="cookbook_detail"),
    path('cookbooks/<int:pk>/update',views.CookbookUpdate.as_view(), name="cookbook_update"),
    path('cookbooks/<int:pk>/delete',views.CookbookDelete.as_view(), name="cookbook_delete"),
    path('cookbooks/<int:pk>/recipes/<int:recipe_pk>/', views.CookbookRecipeAssoc.as_view(), name="cookbook_recipe_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    # path('*', views.Home.as_view(), name="home"),
]