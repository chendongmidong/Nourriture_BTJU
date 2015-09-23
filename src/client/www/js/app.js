// Ionic Nourriture App

angular.module('nourriture', ['ionic', 'nourriture.controllers', 'nourriture.services', 'ngResource'])

.run(function ($ionicPlatform, $window, $http) {

    $window.localStorage.apiUrl = 'http://tossabox.com:8080/api/';

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
})

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
        templateUrl: 'templates/tabs.html'
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

    .state('tab.recipes', {
        url: '/recipes',
        views: {
            'recipes': {
                templateUrl: 'templates/recipes.html',
                controller: 'RecipesCtrl'
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