// Ionic Nourriture App

angular.module('nourriture', ['ionic', 'nourriture.controllers', 'nourriture.services', 'nourriture.tabs', 'nourriture.login', 'ngResource', 'angular-oauth2', 'ngHello'])

.run(function ($ionicPlatform, $window, $http, $rootScope, OAuth, hello) {

    $window.localStorage.apiUrl = 'http://localhost.com:8000/api/';
    // $window.localStorage.apiUrl = 'http://tossabox.com:8080/api/';

    $ionicPlatform.ready(function () {
        // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
        // for form inputs)
        if (window.cordova && window.cordova.plugins && window.cordova.plugins.Keyboard) {
            cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
            cordova.plugins.Keyboard.disableScroll(true);

        }
        if (window.StatusBar) {
            // org.apache.cordova.statusbar required
            StatusBar.styleLightContent();
        }
    });

    // OAtuth 2.0 
    $rootScope.$on('oauth:error', function (event, rejection) {
        // Ignore `invalid_grant` error - should be catched on `LoginController`.
        if ('invalid_grant' === rejection.data.error) {
            return;
        }

        // Refresh token when a `invalid_token` error occurs.
        if ('invalid_token' === rejection.data.error) {
            return OAuth.getRefreshToken();
        }

        // Redirect to `/login` with the `error_reason`.
        return $window.location.href = '/login?error_reason=' + rejection.data.error;
    });

    // Hello
    hello.init({
        google: '650560663671-prj2kpurqa9h59sc4m3cmi03jd76lsj3.apps.googleusercontent.com',
        github: 'https://github.com/login/oauth/authorize'
    }, {
        redirect_uri: '../templates/redirect.html'
    });
})

.config(['OAuthProvider', function (OAuthProvider) {
    OAuthProvider.configure({
        baseUrl: 'http://django-oauth-toolkit.herokuapp.com/consumer/exchange/',
        clientId: '03eca47598e66298fe69',
        clientSecret: 'a51c290d5ea44e728bb00957755e08944ddc1d7f ' // optional
    });
  }])

.config(function ($stateProvider, $urlRouterProvider, $httpProvider, $interpolateProvider, $resourceProvider) {

    /* Python Django config */

    // Change tag symbols, replace {{ }} with [[ ]]
    //    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // Add CSRF Token support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // Don&rsquo;t strip trailing slashes
    $resourceProvider.defaults.stripTrailingSlashes = false;

    /* Python Django config */

    $stateProvider

        .state('login', {
        url: '/login',
        templateUrl: 'templates/login.html',
        controller: 'LoginCtrl'
    })

    // setup an abstract state for the tabs directive
    .state('tab', {
        url: '/tab',
        abstract: true,
        templateUrl: 'templates/tabs.html',
        controller: 'TabsCtrl'
    })

    // Each tab has its own nav history stack:

    .state('tab.login', {
        url: '/login',
        views: {
            'login': {
                templateUrl: 'templates/login.html',
                controller: 'LoginCtrl'
            }
        }
    })

    .state('tab.home', {
        url: '/home',
        views: {
            'home': {
                templateUrl: 'templates/home.html',
                controller: 'HomeCtrl'
            }
        }
    })

    .state('tab.ingredients', {
        url: '/ingredients',
        views: {
            'ingredients': {
                templateUrl: 'templates/ingredients.html',
                controller: 'IngredientsCtrl'
            }
        }
    })

    .state('tab.add-ingredients', {
        url: '/ingredients/add',
        views: {
            'ingredients': {
                templateUrl: 'templates/add-ingredients.html',
                controller: 'AddIngredientsCtrl'
            }
        }
    })

    .state('tab.recipes', {
        url: '/recipes',
        views: {
            'recipes': {
                templateUrl: 'templates/recipes.html',
                controller: 'RecipesCtrl'
            }
        }
    })

    .state('tab.add-recipes', {
        url: '/recipes/add',
        views: {
            'recipes': {
                templateUrl: 'templates/add-recipes.html',
                controller: 'AddRecipesCtrl'
            }
        }
    })

    .state('tab.account', {
        url: '/account',
        views: {
            'account': {
                templateUrl: 'templates/account.html',
                controller: 'AccountCtrl'
            }
        }
    });

    // if none of the above states are matched, use this as the fallback
    $urlRouterProvider.otherwise('/login');

});