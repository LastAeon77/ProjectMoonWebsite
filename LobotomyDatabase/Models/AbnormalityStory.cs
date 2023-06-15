using System.ComponentModel.DataAnnotations.Schema;

namespace LobotomyDatabase.Models
{
	public class AbnormalityStory
	{
		public int ID { get; set; }
		public string? Story { get; set; }
		public string? StoryNumb { get; set; }
		[ForeignKey("Abnormality")]
		public int? AbnormalityID { get; set; }
		public virtual Abnormality? Abnormality { get; set; }
	}
}
