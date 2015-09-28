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

        // set client_id and redirect_uri
        var clientInfo = {
            client_id: 'MyClientId',
            redirect_uri: 'https://rp.example.com/callback.html'
        };
        OIDC.setClientInfo(clientInfo);

        // set Identity Provider configuration information using discovery
        var providerInfo = OIDC.discover('https://op.example.com');

        // or set via manual configuration
        // var providerInfo = {
        //                      issuer: 'https:/op.example.com',
        //                      authorization_endpoint: 'http://op.example.com/auth.html',
        //                      jwks_uri: 'https://op.example.com/jwks'
        //                    };

        // set Identity Provider configuration
        OIDC.setProviderInfo(providerInfo);

        // store configuration for reuse in the callback page
        OIDC.storeInfo(providerInfo, clientInfo);

        // on login error
        //        $window.alert("Hi, login error");

        // on login success
        $rootScope.userType = $scope.roles[$scope.credentials.role - 1].label;
        $state.go('tab.home');
    }
})