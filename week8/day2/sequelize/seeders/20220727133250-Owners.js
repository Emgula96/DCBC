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
    await queryInterface.bulkInsert('Owners',
    [
      {
        name: "Ethan",
        pet:"Callie", 
        clinic:"VCA",
        age: "26",
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        name: "Tommie",
        pet:"Tuna", 
        clinic:"VCA",
        age: "28",
        createdAt: new Date(),
        updatedAt: new Date()
      },

    ],
    {}
  );
},

async down (queryInterface, Sequelize) {
    await queryInterface.bulkDelete("Owners", null, {});
  }
};