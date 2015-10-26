angular.module('nourriture.services', ['ngResource'])

.factory('Recipes', function ($resource, $window) {

    var url = $window.localStorage.apiUrl;

    return {
        byId: function (id, callback) {
            $resource(url + 'recipe/:id').get({
                id: id
            }, function (recipe) {
                callback(recipe.content);
            });
        },
        add: function (recipeData) {
            $http.post(url + 'recipe/add', recipeData, {}).then(function (success) {
                console.log("success", success);
            }, function (error) {
                console.log("error");
            });
        },
        all: function (callback) {
            $resource(url + 'recipe/all').get({}, function (recipes) {
                callback(recipes.content);
            });
        }
    }
})

.factory('Ingredients', function ($http, $resource, $window) {

    var url = $window.localStorage.apiUrl;

    return {
        byId: function (id, callback) {
            $resource(url + 'ingredient/:id').get({
                id: id
            }, function (ingredient) {
                callback(ingredient.content);
            });
        },
        add: function (ingredientData) {
            $http.post(url + 'ingredient/add', ingredientData, {}).then(function (success) {
                console.log("success", success);
            }, function (error) {
                console.log("error");
            });
        },
        all: function (callback) {
            $resource(url + 'ingredient/all').get({}, function (ingredients) {
                callback(ingredients.content);
            });
        }
    }
})

;