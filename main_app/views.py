from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Food, Recipe, Cookbook
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foods"] = Food.objects.filter(user=self.request.user)
        context["recipes"] = Recipe.objects.filter(user=self.request.user)
        context["cookbooks"] = Cookbook.objects.filter(user=self.request.user)
        return context

class About(TemplateView):
    template_name = "about.html"

@method_decorator(login_required, name='dispatch')
class FoodList(TemplateView):
    template_name = "food_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipess"] = Recipe.objects.all()
        name = self.request.GET.get("name")
        if name != None:
            context["foods"] = Food.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["foods"] = Food.objects.filter(user=self.request.user)
            context["header"] = "Popular Foods"
        return context

@method_decorator(login_required, name='dispatch')
class RecipeList(TemplateView):
    template_name = "recipe_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cookbooks"] = Cookbook.objects.filter(user=self.request.user)
        name = self.request.GET.get("name")
        if name != None:
            context["recipes"] = Recipe.objects.filter(name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["recipes"] = Recipe.objects.filter(user=self.request.user)
            context["header"] = "Popular Recipes"
        return context

@method_decorator(login_required, name='dispatch')
class CookbookList(TemplateView):
    template_name = "cookbook_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.filter(user=self.request.user)
        name = self.request.GET.get("name")
        if name != None:
            context["cookbooks"] = Cookbook.objects.filter(name__icontains=name,user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["cookbooks"] = Cookbook.objects.filter(user=self.request.user)
            context["header"] = "Popular Cookbooks"
        return context

class FoodCreate(CreateView):
    model = Food
    fields = ['name', 'image', 'notes', 'favorite_food', 'budget_item', 'pantry_staple', 'kid_approved', 'picky_approved', 'eat_alone', 'sick_friendly', 'low_spoons', 'texture_friendly', 'color_friendly', 'arfid_approved', 'diet_friendly']
    template_name = "food_create.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FoodCreate, self).form_valid(form)
    def get_success_url(self):
        print(self.kwargs)
        return reverse('food_detail', kwargs={'pk': self.object.pk})

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name', 'image', 'directions',  'foods', 'favorite_recipe', 'budget_meal', 'staple_meal', 'kid_approved', 'picky_approved', 'easy_prep', 'sick_friendly', 'low_spoons', 'texture_friendly', 'color_friendly', 'arfid_approved', 'diet_friendly']
    template_name = "recipe_create.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RecipeCreate, self).form_valid(form)
    def get_success_url(self):
        print(self.kwargs)
        return reverse('recipe_detail', kwargs={'pk': self.object.pk})

class CookbookCreate(CreateView):
    model = Cookbook
    fields = ['name', 'image', 'recipes']
    template_name = "cookbook_create.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CookbookCreate, self).form_valid(form)
    def get_success_url(self):
        print(self.kwargs)
        return reverse('cookbook_detail', kwargs={'pk': self.object.pk})

class FoodDetail(DetailView):
    model = Food
    template_name = "food_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.all()
        # context["cookbooks"] = Cookbook.objects.all()
        return context

class RecipeDetail(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foods"] = Food.objects.all()
        # context["recipes"] = Recipe.objects.all()
        context["cookbooks"] = Cookbook.objects.all()
        return context

class CookbookDetail(DetailView):
    model = Cookbook
    template_name = "cookbook_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipe.objects.all()
        return context

class FoodUpdate(UpdateView):
    model = Food
    fields = ['name', 'image', 'notes', 'favorite_food', 'budget_item', 'pantry_staple', 'kid_approved', 'picky_approved', 'eat_alone', 'sick_friendly', 'low_spoons', 'texture_friendly', 'color_friendly', 'arfid_approved', 'diet_friendly']
    template_name = "food_update.html"
    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'image', 'directions', 'foods', 'favorite_recipe', 'budget_meal', 'staple_meal', 'kid_approved', 'picky_approved', 'easy_prep', 'sick_friendly', 'low_spoons', 'texture_friendly', 'color_friendly', 'arfid_approved', 'diet_friendly']
    template_name = "recipe_update.html"
    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.object.pk})

class CookbookUpdate(UpdateView):
    model = Cookbook
    fields = ['name', 'image', 'recipes']
    template_name = "cookbook_update.html"
    def get_success_url(self):
        return reverse('cookbook_detail', kwargs={'pk': self.object.pk})

class FoodDelete(DeleteView):
    model = Food
    template_name = "food_delete_confirmation.html"
    success_url = "/foods/"

class RecipeDelete(DeleteView):
    model = Recipe
    template_name = "recipe_delete_confirmation.html"
    success_url = "/recipes/"

class CookbookDelete(DeleteView):
    model = Cookbook
    template_name = "cookbook_delete_confirmation.html"
    success_url = "/cookbooks/"

class RecipeFoodAssoc(View):

    def get(self, request, pk, food_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Recipe.objects.get(pk=pk).foods.remove(food_pk)
        if assoc == "add":
            Recipe.objects.get(pk=pk).foods.add(food_pk)
        return redirect('/recipes/')

class CookbookRecipeAssoc(View):

    def get(self, request, pk, recipe_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Cookbook.objects.get(pk=pk).recipes.remove(recipe_pk)
        if assoc == "add":
            Cookbook.objects.get(pk=pk).recipes.add(recipe_pk)
        return redirect('/cookbooks/')

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form ssubmit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("food_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

def view_404(request, exception=None):
    return redirect('about')