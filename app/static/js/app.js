// Declare app level module which depends on filters, and services
angular.module('plo', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date', 'google-maps'])
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/pages/home.html',
        controller: 'HomeController'})
      .when('/resource-library', {
        templateUrl: 'views/pages/resource-library.html',
        controller: 'ResourceLibraryController'})
      .when('/testimonials/:person', {
        templateUrl: function (params) {
          return 'views/pages/testimonials/' + params.person + '.html';
        },
        controller: 'TestimonialsController'})
      .when('/testimonials', {
        templateUrl: 'views/pages/testimonials.html',
        controller: 'TestimonialsController'})
      .when('/find-a-doctor', {
        templateUrl: 'views/pages/find-a-doctor.html',
        controller: 'FindDoctorController'})
      .otherwise({redirectTo: '/'});
  }]);
