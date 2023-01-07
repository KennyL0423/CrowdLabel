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

/**
 * The RegistrationRequest model module.
 * @module model/RegistrationRequest
 * @version 0.1.0
 */
class RegistrationRequest {
    /**
     * Constructs a new <code>RegistrationRequest</code>.
     * @alias module:model/RegistrationRequest
     * @param verificationCode {String} 
     * @param userType {String} 
     * @param password {String} 
     * @param email {String} 
     * @param username {String} 
     */
    constructor(verificationCode, userType, password, email, username) { 
        
        RegistrationRequest.initialize(this, verificationCode, userType, password, email, username);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, verificationCode, userType, password, email, username) { 
        obj['verification_code'] = verificationCode;
        obj['user_type'] = userType;
        obj['password'] = password;
        obj['email'] = email;
        obj['username'] = username;
    }

    /**
     * Constructs a <code>RegistrationRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RegistrationRequest} obj Optional instance to populate.
     * @return {module:model/RegistrationRequest} The populated <code>RegistrationRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RegistrationRequest();

            if (data.hasOwnProperty('verification_code')) {
                obj['verification_code'] = ApiClient.convertToType(data['verification_code'], 'String');
            }
            if (data.hasOwnProperty('user_type')) {
                obj['user_type'] = ApiClient.convertToType(data['user_type'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('username')) {
                obj['username'] = ApiClient.convertToType(data['username'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RegistrationRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RegistrationRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RegistrationRequest.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['verification_code'] && !(typeof data['verification_code'] === 'string' || data['verification_code'] instanceof String)) {
            throw new Error("Expected the field `verification_code` to be a primitive type in the JSON string but got " + data['verification_code']);
        }
        // ensure the json data is a string
        if (data['user_type'] && !(typeof data['user_type'] === 'string' || data['user_type'] instanceof String)) {
            throw new Error("Expected the field `user_type` to be a primitive type in the JSON string but got " + data['user_type']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['username'] && !(typeof data['username'] === 'string' || data['username'] instanceof String)) {
            throw new Error("Expected the field `username` to be a primitive type in the JSON string but got " + data['username']);
        }

        return true;
    }


}

RegistrationRequest.RequiredProperties = ["verification_code", "user_type", "password", "email", "username"];

/**
 * @member {String} verification_code
 */
RegistrationRequest.prototype['verification_code'] = undefined;

/**
 * @member {String} user_type
 */
RegistrationRequest.prototype['user_type'] = undefined;

/**
 * @member {String} password
 */
RegistrationRequest.prototype['password'] = undefined;

/**
 * @member {String} email
 */
RegistrationRequest.prototype['email'] = undefined;

/**
 * @member {String} username
 */
RegistrationRequest.prototype['username'] = undefined;






export default RegistrationRequest;
