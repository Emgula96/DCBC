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
      "Clients", 
      [
        {
        firstName: 'John',
        lastName: 'Doe',
        email: 'fakeemail@hotmail.com',
        pet: "doggie",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
        {
        firstName: 'Jane',
        lastName: 'Doe',
        email: 'fakeemail@hotmail.com',
        pet: 'kitty',
        createdAt: new Date(),
        updatedAt: new Date(),
      },
        {
        firstName: 'Joe',
        lastName: 'Doe',
        email: 'fakeemail@hotmail.com',
        pet: 'fishy',
        createdAt: new Date(),
        updatedAt: new Date(),
      },
        {
        firstName: 'Jamie',
        lastName: 'Doe',
        email: 'fakeemail@hotmail.com',
        pet: 'rock',
        createdAt: new Date(),
        updatedAt: new Date(),
      },
    ],
    {}
    );
  
    },

  async down (queryInterface, Sequelize) {
    await queryInterface.bulkDelete("Clients", null, {});
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
  }
};
