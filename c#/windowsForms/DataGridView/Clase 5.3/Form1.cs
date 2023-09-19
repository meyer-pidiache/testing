using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Clase_5._3
{
    public partial class Form1 : Form
    {
        private int n = 0;
        public Form1()
        {
            InitializeComponent();
        }

        private void buttonAdicionar_Click(object sender, EventArgs e)
        {
            int n = dataGridView1.Rows.Add();

            dataGridView1.Rows[n].Cells[0].Value = textBoxCodigo.Text;
            dataGridView1.Rows[n].Cells[1].Value = textBoxNombre.Text;
            dataGridView1.Rows[n].Cells[2].Value = textBoxPrecio.Text;

            textBoxCodigo.Text = "";
            textBoxNombre.Text = "";
            textBoxPrecio.Text = "";
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            n = e.RowIndex;

            if (n != -1)
            {
                labelInformacion.Text = (string)dataGridView1.Rows[n].Cells[1].Value;
            }
        }

        private void buttonBorrar_Click(object sender, EventArgs e)
        {
            if (n != -1)
            {
                dataGridView1.Rows.RemoveAt(n);
            }
        }

        private void buttonSumar_Click(object sender, EventArgs e)
        {
            double resultado = 0;

            foreach (DataGridViewRow row in dataGridView1.Rows)
            {
                resultado += Convert.ToDouble(row.Cells["Precio"].Value);
            }

            MessageBox.Show("La suma de los precios de los productos es $" + resultado);
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
