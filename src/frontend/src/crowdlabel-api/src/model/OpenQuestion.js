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

import ApiClient from '../ApiClient';
import OpenAnswer from './OpenAnswer';

/**
 * The OpenQuestion model module.
 * @module model/OpenQuestion
 * @version 0.1.0
 */
class OpenQuestion {
    /**
     * Constructs a new <code>OpenQuestion</code>.
     * @alias module:model/OpenQuestion
     * @param questionId {Number} 
     * @param prompt {String} 
     */
    constructor(questionId, prompt) { 
        
        OpenQuestion.initialize(this, questionId, prompt);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, questionId, prompt) { 
        obj['question_id'] = questionId;
        obj['prompt'] = prompt;
    }

    /**
     * Constructs a <code>OpenQuestion</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OpenQuestion} obj Optional instance to populate.
     * @return {module:model/OpenQuestion} The populated <code>OpenQuestion</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OpenQuestion();

            if (data.hasOwnProperty('question_id')) {
                obj['question_id'] = ApiClient.convertToType(data['question_id'], 'Number');
            }
            if (data.hasOwnProperty('question_type')) {
                obj['question_type'] = ApiClient.convertToType(data['question_type'], 'String');
            }
            if (data.hasOwnProperty('prompt')) {
                obj['prompt'] = ApiClient.convertToType(data['prompt'], 'String');
            }
            if (data.hasOwnProperty('resource')) {
                obj['resource'] = ApiClient.convertToType(data['resource'], 'String');
            }
            if (data.hasOwnProperty('answers')) {
                obj['answers'] = ApiClient.convertToType(data['answers'], [OpenAnswer]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OpenQuestion</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OpenQuestion</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of OpenQuestion.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['question_type'] && !(typeof data['question_type'] === 'string' || data['question_type'] instanceof String)) {
            throw new Error("Expected the field `question_type` to be a primitive type in the JSON string but got " + data['question_type']);
        }
        // ensure the json data is a string
        if (data['prompt'] && !(typeof data['prompt'] === 'string' || data['prompt'] instanceof String)) {
            throw new Error("Expected the field `prompt` to be a primitive type in the JSON string but got " + data['prompt']);
        }
        // ensure the json data is a string
        if (data['resource'] && !(typeof data['resource'] === 'string' || data['resource'] instanceof String)) {
            throw new Error("Expected the field `resource` to be a primitive type in the JSON string but got " + data['resource']);
        }
        if (data['answers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['answers'])) {
                throw new Error("Expected the field `answers` to be an array in the JSON data but got " + data['answers']);
            }
            // validate the optional field `answers` (array)
            for (const item of data['answers']) {
                OpenAnswer.validateJsonObject(item);
            };
        }

        return true;
    }


}

OpenQuestion.RequiredProperties = ["question_id", "prompt"];

/**
 * @member {Number} question_id
 */
OpenQuestion.prototype['question_id'] = undefined;

/**
 * @member {String} question_type
 * @default 'open'
 */
OpenQuestion.prototype['question_type'] = 'open';

/**
 * @member {String} prompt
 */
OpenQuestion.prototype['prompt'] = undefined;

/**
 * @member {String} resource
 */
OpenQuestion.prototype['resource'] = undefined;

/**
 * @member {Array.<module:model/OpenAnswer>} answers
 */
OpenQuestion.prototype['answers'] = undefined;






export default OpenQuestion;
