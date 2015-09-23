angular.module('nourriture.controllers', [])

.controller('LoginCtrl', function ($scope, $state) {

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
        console.info("Hi", $scope.credentials.role, $scope.credentials.username, "!");
        console.info("Your password is [", $scope.credentials.password, "]");
        console.info("Using OpenID here, soon.");
        $state.go('tab.home');
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

.controller('ChatsCtrl', function ($scope, Chats) {
    // With the new view caching in Ionic, Controllers are only called
    // when they are recreated or on app start, instead of every page change.
    // To listen for when this page is active (for example, to refresh data),
    // listen for the $ionicView.enter event:
    //
    //$scope.$on('$ionicView.enter', function(e) {
    //});

    $scope.chats = Chats.all();
    $scope.remove = function (chat) {
        Chats.remove(chat);
    };
})

.controller('ChatDetailCtrl', function ($scope, $stateParams, Chats) {
    $scope.chat = Chats.get($stateParams.chatId);
})

.controller('AccountCtrl', function ($scope) {
    $scope.settings = {
        enableFriends: true
    };
});