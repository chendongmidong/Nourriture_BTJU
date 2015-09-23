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
        all: function (callback) {
            $resource(url + 'recipe/all').get({}, function (recipes) {
                callback(recipes.content);
            });
        }
    }
})

.factory('Ingredients', function ($resource, $window) {

    var url = $window.localStorage.apiUrl;

    return {
        byId: function (id, callback) {
            $resource(url + 'ingredient/:id').get({
                id: id
            }, function (ingredient) {
                callback(ingredient.content);
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