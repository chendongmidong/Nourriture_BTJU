angular.module('nourriture.controllers', [])

.controller('LoginCtrl', function ($scope, $state, $rootScope) {

    $scope.roles = [
        {
            id: 1,
            label: 'Food Consumer'
        },
        {
            id: 2,
            label: 'Food Supplier'
        },
        {
            id: 3,
            label: 'Gastronomist'
        },
    ]

    $scope.credentials = {
        username: "",
        password: "",
        role: 1
    };

    $scope.login = function () {
        console.info($scope.roles[$scope.credentials.role - 1].id);
        console.info("Hi", $scope.roles[$scope.credentials.role - 1].label, $scope.credentials.username, "!");
        console.info("Your password is [", $scope.credentials.password, "]");
        console.info("Using OpenID here, soon.");
        $state.go('tab.home');
        $rootScope.userType = $scope.roles[$scope.credentials.role - 1].label;
    }

})

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