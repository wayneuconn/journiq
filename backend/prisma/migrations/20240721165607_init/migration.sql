-- CreateEnum
CREATE TYPE "ItemStatus" AS ENUM ('packed', 'not_packed');

-- CreateEnum
CREATE TYPE "TransportMethod" AS ENUM ('flight', 'train', 'car_rental');

-- CreateEnum
CREATE TYPE "Role" AS ENUM ('admin', 'member');

-- CreateTable
CREATE TABLE "Member" (
    "memberUID" UUID NOT NULL,
    "nickName" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "role" "Role" NOT NULL DEFAULT 'member',

    CONSTRAINT "Member_pkey" PRIMARY KEY ("memberUID")
);

-- CreateTable
CREATE TABLE "Group" (
    "groupUID" UUID NOT NULL,
    "name" TEXT NOT NULL,

    CONSTRAINT "Group_pkey" PRIMARY KEY ("groupUID")
);

-- CreateTable
CREATE TABLE "GroupMember" (
    "groupUID" UUID NOT NULL,
    "memberUID" UUID NOT NULL,

    CONSTRAINT "GroupMember_pkey" PRIMARY KEY ("groupUID","memberUID")
);

-- CreateIndex
CREATE UNIQUE INDEX "Member_email_key" ON "Member"("email");

-- AddForeignKey
ALTER TABLE "GroupMember" ADD CONSTRAINT "GroupMember_groupUID_fkey" FOREIGN KEY ("groupUID") REFERENCES "Group"("groupUID") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "GroupMember" ADD CONSTRAINT "GroupMember_memberUID_fkey" FOREIGN KEY ("memberUID") REFERENCES "Member"("memberUID") ON DELETE RESTRICT ON UPDATE CASCADE;
