angular.module('nourriture.login', ['ngResource', 'ngHello'])

.controller('LoginCtrl', function ($scope, $state, $rootScope, $window, hello) {

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

    $scope.login = function (network) {
        //        console.info($scope.roles[$scope.credentials.role - 1].id);
        console.info("Hi", $scope.roles[$scope.credentials.role - 1].label);
        console.info("Network:", network);
        hello.login(network);

        // on login error
        //        $window.alert("Hi, login error");

        // on login success
        $rootScope.userType = $scope.roles[$scope.credentials.role - 1].label;
                $state.go('tab.home');
    }
})