import type { JestConfigWithTsJest } from 'ts-jest';

const config: JestConfigWithTsJest = {
  testEnvironment: "jsdom",
  transform: {
    "^.+\\.tsx?$": [
      "ts-jest",
      {
        tsconfig: "<rootDir>/tsconfig.app.json",
      },
    ],
  },
  setupFilesAfterEnv: ["<rootDir>/jest.setup.ts"],
  moduleNameMapper: {
    '^~/(.*)$': '<rootDir>/app/$1',
  },
};

export default config;