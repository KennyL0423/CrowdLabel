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
 * The EditEmailRequest model module.
 * @module model/EditEmailRequest
 * @version 0.1.0
 */
class EditEmailRequest {
    /**
     * Constructs a new <code>EditEmailRequest</code>.
     * @alias module:model/EditEmailRequest
     * @param newEmail {String} 
     * @param verificationCode {String} 
     * @param password {String} 
     */
    constructor(newEmail, verificationCode, password) { 
        
        EditEmailRequest.initialize(this, newEmail, verificationCode, password);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, newEmail, verificationCode, password) { 
        obj['new_email'] = newEmail;
        obj['verification_code'] = verificationCode;
        obj['password'] = password;
    }

    /**
     * Constructs a <code>EditEmailRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EditEmailRequest} obj Optional instance to populate.
     * @return {module:model/EditEmailRequest} The populated <code>EditEmailRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EditEmailRequest();

            if (data.hasOwnProperty('new_email')) {
                obj['new_email'] = ApiClient.convertToType(data['new_email'], 'String');
            }
            if (data.hasOwnProperty('verification_code')) {
                obj['verification_code'] = ApiClient.convertToType(data['verification_code'], 'String');
            }
            if (data.hasOwnProperty('password')) {
                obj['password'] = ApiClient.convertToType(data['password'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EditEmailRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EditEmailRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EditEmailRequest.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['new_email'] && !(typeof data['new_email'] === 'string' || data['new_email'] instanceof String)) {
            throw new Error("Expected the field `new_email` to be a primitive type in the JSON string but got " + data['new_email']);
        }
        // ensure the json data is a string
        if (data['verification_code'] && !(typeof data['verification_code'] === 'string' || data['verification_code'] instanceof String)) {
            throw new Error("Expected the field `verification_code` to be a primitive type in the JSON string but got " + data['verification_code']);
        }
        // ensure the json data is a string
        if (data['password'] && !(typeof data['password'] === 'string' || data['password'] instanceof String)) {
            throw new Error("Expected the field `password` to be a primitive type in the JSON string but got " + data['password']);
        }

        return true;
    }


}

EditEmailRequest.RequiredProperties = ["new_email", "verification_code", "password"];

/**
 * @member {String} new_email
 */
EditEmailRequest.prototype['new_email'] = undefined;

/**
 * @member {String} verification_code
 */
EditEmailRequest.prototype['verification_code'] = undefined;

/**
 * @member {String} password
 */
EditEmailRequest.prototype['password'] = undefined;






export default EditEmailRequest;

