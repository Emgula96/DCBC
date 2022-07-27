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
    await queryInterface.bulkInsert('Pets',
    [
      {
        name: "Callie",
        species: "dog",
        age: "3",
        weight: 35,
        health: "healthy",
        unitOfWeight: "lbs",
        owner: "Ethan",
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        name: "Scoodles",
        species: "cat",
        age: "10",
        weight: 10,
        health: "healthy",
        unitOfWeight: "lbs",
        owner: "Ethan",
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        name: "Tuna",
        species: "cat",
        age: "6",
        weight: 30,
        health: "healthy",
        unitOfWeight: "lbs",
        owner: "Tommie",
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        name: "George Harrison",
        species: "fish",
        age: "1",
        weight: 1,
        health: "healthy",
        unitOfWeight: "lbs",
        owner: "Tommie",
        createdAt: new Date(),
        updatedAt: new Date()
      },
      {
        name: "Tobi",
        species: "dog",
        age: "1",
        weight: 55,
        health: "healthy",
        unitOfWeight: "lbs",
        owner: "Diep",
        createdAt: new Date(),
        updatedAt: new Date()
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
    await queryInterface.bulkDelete("Pets", null, {});
    },
  };
