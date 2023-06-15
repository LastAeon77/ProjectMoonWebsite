﻿// <auto-generated />
using System;
using LobotomyDatabase.Data;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace LobotomyDatabase.Migrations
{
    [DbContext(typeof(LobotomyData))]
    partial class LobotomyDataModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "7.0.7")
                .HasAnnotation("Relational:MaxIdentifierLength", 63);

            NpgsqlModelBuilderExtensions.UseIdentityByDefaultColumns(modelBuilder);

            modelBuilder.Entity("LobotomyDatabase.Models.Abnormality", b =>
                {
                    b.Property<int>("ID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("integer");

                    NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b.Property<int>("ID"));

                    b.Property<string>("Name")
                        .HasColumnType("text");

                    b.Property<string>("NumCode")
                        .HasColumnType("text");

                    b.Property<string>("OpenText")
                        .HasColumnType("text");

                    b.Property<int?>("RiskLevel")
                        .HasColumnType("integer");

                    b.Property<string>("in_game_id")
                        .HasColumnType("text");

                    b.HasKey("ID");

                    b.ToTable("Abnormality", (string)null);
                });

            modelBuilder.Entity("LobotomyDatabase.Models.AbnormalityNarration", b =>
                {
                    b.Property<int>("ID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("integer");

                    NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b.Property<int>("ID"));

                    b.Property<int?>("AbnormalityID")
                        .HasColumnType("integer");

                    b.Property<string>("Narration")
                        .HasColumnType("text");

                    b.Property<string>("NarrationAction")
                        .HasColumnType("text");

                    b.HasKey("ID");

                    b.HasIndex("AbnormalityID");

                    b.ToTable("AbnormalityNarration", (string)null);
                });

            modelBuilder.Entity("LobotomyDatabase.Models.AbnormalityStory", b =>
                {
                    b.Property<int>("ID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("integer");

                    NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b.Property<int>("ID"));

                    b.Property<int?>("AbnormalityID")
                        .HasColumnType("integer");

                    b.Property<string>("Story")
                        .HasColumnType("text");

                    b.Property<string>("StoryNumb")
                        .HasColumnType("text");

                    b.HasKey("ID");

                    b.HasIndex("AbnormalityID");

                    b.ToTable("AbnormalityStory", (string)null);
                });

            modelBuilder.Entity("LobotomyDatabase.Models.AbnormalityTip", b =>
                {
                    b.Property<int>("ID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("integer");

                    NpgsqlPropertyBuilderExtensions.UseIdentityByDefaultColumn(b.Property<int>("ID"));

                    b.Property<int?>("AbnormalityID")
                        .HasColumnType("integer");

                    b.Property<string>("Tip")
                        .HasColumnType("text");

                    b.Property<string>("TipNum")
                        .HasColumnType("text");

                    b.HasKey("ID");

                    b.HasIndex("AbnormalityID");

                    b.ToTable("AbnormalityTip", (string)null);
                });

            modelBuilder.Entity("LobotomyDatabase.Models.AbnormalityNarration", b =>
                {
                    b.HasOne("LobotomyDatabase.Models.Abnormality", "Abnormality")
                        .WithMany("Narrations")
                        .HasForeignKey("AbnormalityID");

                    b.Navigation("Abnormality");
                });

            modelBuilder.Entity("LobotomyDatabase.Models.AbnormalityStory", b =>
                {
                    b.HasOne("LobotomyDatabase.Models.Abnormality", "Abnormality")
                        .WithMany("Stories")
                        .HasForeignKey("AbnormalityID");

                    b.Navigation("Abnormality");
                });

            modelBuilder.Entity("LobotomyDatabase.Models.AbnormalityTip", b =>
                {
                    b.HasOne("LobotomyDatabase.Models.Abnormality", "Abnormality")
                        .WithMany("Tips")
                        .HasForeignKey("AbnormalityID");

                    b.Navigation("Abnormality");
                });

            modelBuilder.Entity("LobotomyDatabase.Models.Abnormality", b =>
                {
                    b.Navigation("Narrations");

                    b.Navigation("Stories");

                    b.Navigation("Tips");
                });
#pragma warning restore 612, 618
        }
    }
}
