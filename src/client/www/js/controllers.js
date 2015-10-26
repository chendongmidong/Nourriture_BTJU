angular.module('nourriture.controllers', [])

.controller('HomeCtrl', function ($scope, Ingredients) {

    Ingredients.byId(3, function (ingredient) {
        $scope.ingredientById = ingredient;
    });

    Ingredients.all(function (ingredients) {
        $scope.ingredients = ingredients;
    });
})

.controller('IngredientsCtrl', function ($scope, $state, Ingredients) {

    Ingredients.byId(3, function (ingredient) {
        $scope.ingredientById = ingredient;
    });

    Ingredients.all(function (ingredients) {
        $scope.ingredients = ingredients;
    });

    $scope.go = function (path) {
        $state.go(path);
    }
})

.controller('AddIngredientsCtrl', function ($scope, Ingredients) {

    $scope.ingredientObj = {
        name: "",
        description: "",
        price: "",
        heat: "",
        protein: "",
        fat: "",
        carbohydrate: "",
        vitamin: ""
    };

    $scope.addIngredient = function (ingredientData) {
        Ingredients.add(ingredientData);
        console.log($scope.ingredientObj);
        console.info("in addIngredient");
    }
    console.log("AddIngredientsCtrl");
})

.controller('AddRecipesCtrl', function ($scope, Ingredients) {

    $scope.recipeObj = {
        name: "",
        description: "",
        price: "",
        heat: "",
        protein: "",
        fat: "",
        carbohydrate: "",
        vitamin: ""
    };

    $scope.addRecipe = function (recipeData) {
        Recipes.add(recipeData);
        console.log($scope.recipeObj);
        console.info("in addRecipe");
    }
    console.log("AddIngredientsCtrl");
})

.controller('RecipesCtrl', function ($scope, $state, Recipes) {

    Recipes.all(function (recipes) {
        $scope.recipes = recipes;
    });

    $scope.go = function (path) {
        $state.go(path);
    }
})

.controller('AccountCtrl', function ($scope) {
    $scope.user = {
        string: 'string',
        num: 5,
        bool: true
    };
});