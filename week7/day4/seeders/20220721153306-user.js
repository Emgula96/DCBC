'use strict';

module.exports = {
  async up (queryInterface, Sequelize) {
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
    */
    await queryInterface.bulkInsert(
      "Users", 
    [
      {
      firstName: 'John',
      lastName: 'Doe',
      email: 'Joe@john.com',
      createdAt: new Date(),
      updatedAt: new Date(),
    },
      {
      firstName: 'Jane',
      lastName: 'Doe',
      email: 'Jane@john.com',
      createdAt: new Date(),
      updatedAt: new Date(),
    },
      {
      firstName: 'Joe',
      lastName: 'Doe',
      email: 'Joe@Doe.com',
      createdAt: new Date(),
      updatedAt: new Date(),
    },
      {
      firstName: 'Jamie',
      lastName: 'Doe',
      email: 'Jamie@john.com',
      createdAt: new Date(),
      updatedAt: new Date(),
    },
  ],
  {}
  );

  },

  async down (queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
    await queryInterface.bulkDelete('People', null, {});
  }
};
