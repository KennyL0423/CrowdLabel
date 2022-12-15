/**
 * CrowdLabelAPI
 * API for CrowdLabel
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.CrowdLabelApi);
  }
}(this, function(expect, CrowdLabelApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CrowdLabelApi.Answer();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('Answer', function() {
    it('should create an instance of Answer', function() {
      // uncomment below and update the code to test Answer
      //var instance = new CrowdLabelApi.Answer();
      //expect(instance).to.be.a(CrowdLabelApi.Answer);
    });

    it('should have the property respondent (base name: "respondent")', function() {
      // uncomment below and update the code to test the property respondent
      //var instance = new CrowdLabelApi.Answer();
      //expect(instance).to.be();
    });

    it('should have the property dateAnswered (base name: "date_answered")', function() {
      // uncomment below and update the code to test the property dateAnswered
      //var instance = new CrowdLabelApi.Answer();
      //expect(instance).to.be();
    });

    it('should have the property taskId (base name: "task_id")', function() {
      // uncomment below and update the code to test the property taskId
      //var instance = new CrowdLabelApi.Answer();
      //expect(instance).to.be();
    });

    it('should have the property questionId (base name: "question_id")', function() {
      // uncomment below and update the code to test the property questionId
      //var instance = new CrowdLabelApi.Answer();
      //expect(instance).to.be();
    });

    it('should have the property questionType (base name: "question_type")', function() {
      // uncomment below and update the code to test the property questionType
      //var instance = new CrowdLabelApi.Answer();
      //expect(instance).to.be();
    });

    it('should have the property answer (base name: "answer")', function() {
      // uncomment below and update the code to test the property answer
      //var instance = new CrowdLabelApi.Answer();
      //expect(instance).to.be();
    });

  });

}));