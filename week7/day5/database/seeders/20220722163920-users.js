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
  await queryInterface.bulkInsert('Users',[
    {
      firstName: "Joe",
      lastName:"Coolguy",
      email:"jwfrasier@hotmail.com",
      password:"fakepassword",
      createdAt: new Date(),
      updatedAt: new Date(),
    },
    {
      firstName: "BLK",
      lastName:"Guy",
      email:"blk6959@hotmail.com",
      password:"fakepassword",
      createdAt: new Date(),
      updatedAt: new Date(),
    },
  ],{}
  );
  },

  async down (queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
    await queryInterface.bulkDelete("Users",null,
    {});
  },
};
