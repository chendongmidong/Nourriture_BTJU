angular.module('nourriture.controllers', [])

.controller('HomeCtrl', function ($scope, Ingredients) {

    Ingredients.byId(3, function (ingredient) {
        $scope.ingredientById = ingredient;
    });

    Ingredients.all(function (ingredients) {
        $scope.ingredients = ingredients;
    });
})

.controller('IngredientsCtrl', function ($scope, Ingredients) {

    Ingredients.byId(3, function (ingredient) {
        $scope.ingredientById = ingredient;
    });

    Ingredients.all(function (ingredients) {
        $scope.ingredients = ingredients;
    });
})

.controller('RecipesCtrl', function ($scope, Recipes) {

    Recipes.all(function (recipes) {
        $scope.recipes = recipes;
    });
})

.controller('AccountCtrl', function ($scope) {
    $scope.settings = {
        enableFriends: true
    };
});