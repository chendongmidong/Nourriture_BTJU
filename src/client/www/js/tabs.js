angular.module('nourriture.tabs', ['ngResource'])

.controller('TabsCtrl', function ($scope, $rootScope) {

    if ($rootScope.userType == undefined) {
        $rootScope.userType = 'Food Consumer';
    }

    $rootScope.$on('$ionicView.beforeEnter', function () {
        if ($rootScope.userType === 'Food Consumer') {
            $scope.tabOnUserType = {
                home: false,
                ingredients: false,
                recipes: false
            };
        }

        if ($rootScope.userType === 'Food Supplier') {
            $scope.tabOnUserType = {
                home: false,
                ingredients: false,
                recipes: true
            };
        }

        if ($rootScope.userType === 'Gastronomist') {
            $scope.tabOnUserType = {
                home: false,
                ingredients: true,
                recipes: false
            };
        }
    })
})