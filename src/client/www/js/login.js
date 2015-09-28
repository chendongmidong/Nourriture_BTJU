angular.module('nourriture.login', ['ngResource'])

.controller('LoginCtrl', function ($scope, $state, $rootScope, $window) {

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
        //        console.info($scope.roles[$scope.credentials.role - 1].id);
        console.info("Hi", $scope.roles[$scope.credentials.role - 1].label, $scope.credentials.username, "!");
        console.info("Your password is [", $scope.credentials.password, "]");
        console.info("Using OpenID here, soon.");

        // on login error
        //        $window.alert("Hi, login error");

        // on login success
        $rootScope.userType = $scope.roles[$scope.credentials.role - 1].label;
        $state.go('tab.home');
    }
})