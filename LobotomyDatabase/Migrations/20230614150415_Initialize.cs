using Microsoft.EntityFrameworkCore.Migrations;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

#nullable disable

namespace LobotomyDatabase.Migrations
{
    /// <inheritdoc />
    public partial class Initialize : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Abnormality",
                columns: table => new
                {
                    ID = table.Column<int>(type: "integer", nullable: false)
                        .Annotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.IdentityByDefaultColumn),
                    in_game_id = table.Column<string>(type: "text", nullable: true),
                    Name = table.Column<string>(type: "text", nullable: true),
                    NumCode = table.Column<string>(type: "text", nullable: true),
                    RiskLevel = table.Column<int>(type: "integer", nullable: true),
                    OpenText = table.Column<string>(type: "text", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Abnormality", x => x.ID);
                });

            migrationBuilder.CreateTable(
                name: "AbnormalityNarration",
                columns: table => new
                {
                    ID = table.Column<int>(type: "integer", nullable: false)
                        .Annotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.IdentityByDefaultColumn),
                    Narration = table.Column<string>(type: "text", nullable: true),
                    NarrationAction = table.Column<string>(type: "text", nullable: true),
                    AbnormalityID = table.Column<int>(type: "integer", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AbnormalityNarration", x => x.ID);
                    table.ForeignKey(
                        name: "FK_AbnormalityNarration_Abnormality_AbnormalityID",
                        column: x => x.AbnormalityID,
                        principalTable: "Abnormality",
                        principalColumn: "ID");
                });

            migrationBuilder.CreateTable(
                name: "AbnormalityStory",
                columns: table => new
                {
                    ID = table.Column<int>(type: "integer", nullable: false)
                        .Annotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.IdentityByDefaultColumn),
                    Story = table.Column<string>(type: "text", nullable: true),
                    StoryNumb = table.Column<string>(type: "text", nullable: true),
                    AbnormalityID = table.Column<int>(type: "integer", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AbnormalityStory", x => x.ID);
                    table.ForeignKey(
                        name: "FK_AbnormalityStory_Abnormality_AbnormalityID",
                        column: x => x.AbnormalityID,
                        principalTable: "Abnormality",
                        principalColumn: "ID");
                });

            migrationBuilder.CreateTable(
                name: "AbnormalityTip",
                columns: table => new
                {
                    ID = table.Column<int>(type: "integer", nullable: false)
                        .Annotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.IdentityByDefaultColumn),
                    Tip = table.Column<string>(type: "text", nullable: true),
                    TipNum = table.Column<string>(type: "text", nullable: true),
                    AbnormalityID = table.Column<int>(type: "integer", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AbnormalityTip", x => x.ID);
                    table.ForeignKey(
                        name: "FK_AbnormalityTip_Abnormality_AbnormalityID",
                        column: x => x.AbnormalityID,
                        principalTable: "Abnormality",
                        principalColumn: "ID");
                });

            migrationBuilder.CreateIndex(
                name: "IX_AbnormalityNarration_AbnormalityID",
                table: "AbnormalityNarration",
                column: "AbnormalityID");

            migrationBuilder.CreateIndex(
                name: "IX_AbnormalityStory_AbnormalityID",
                table: "AbnormalityStory",
                column: "AbnormalityID");

            migrationBuilder.CreateIndex(
                name: "IX_AbnormalityTip_AbnormalityID",
                table: "AbnormalityTip",
                column: "AbnormalityID");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "AbnormalityNarration");

            migrationBuilder.DropTable(
                name: "AbnormalityStory");

            migrationBuilder.DropTable(
                name: "AbnormalityTip");

            migrationBuilder.DropTable(
                name: "Abnormality");
        }
    }
}
